// ORM class for table 'drivers'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Fri May 27 15:37:46 UTC 2022
// For connector: org.apache.sqoop.manager.MySQLManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import com.cloudera.sqoop.lib.JdbcWritableBridge;
import com.cloudera.sqoop.lib.DelimiterSet;
import com.cloudera.sqoop.lib.FieldFormatter;
import com.cloudera.sqoop.lib.RecordParser;
import com.cloudera.sqoop.lib.BooleanParser;
import com.cloudera.sqoop.lib.BlobRef;
import com.cloudera.sqoop.lib.ClobRef;
import com.cloudera.sqoop.lib.LargeObjectLoader;
import com.cloudera.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class drivers extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("driverId", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.driverId = (Integer)value;
      }
    });
    setters.put("name", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.name = (String)value;
      }
    });
    setters.put("ssn", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.ssn = (String)value;
      }
    });
    setters.put("location", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.location = (String)value;
      }
    });
    setters.put("certified", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.certified = (String)value;
      }
    });
    setters.put("wage_plan", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        drivers.this.wage_plan = (String)value;
      }
    });
  }
  public drivers() {
    init0();
  }
  private Integer driverId;
  public Integer get_driverId() {
    return driverId;
  }
  public void set_driverId(Integer driverId) {
    this.driverId = driverId;
  }
  public drivers with_driverId(Integer driverId) {
    this.driverId = driverId;
    return this;
  }
  private String name;
  public String get_name() {
    return name;
  }
  public void set_name(String name) {
    this.name = name;
  }
  public drivers with_name(String name) {
    this.name = name;
    return this;
  }
  private String ssn;
  public String get_ssn() {
    return ssn;
  }
  public void set_ssn(String ssn) {
    this.ssn = ssn;
  }
  public drivers with_ssn(String ssn) {
    this.ssn = ssn;
    return this;
  }
  private String location;
  public String get_location() {
    return location;
  }
  public void set_location(String location) {
    this.location = location;
  }
  public drivers with_location(String location) {
    this.location = location;
    return this;
  }
  private String certified;
  public String get_certified() {
    return certified;
  }
  public void set_certified(String certified) {
    this.certified = certified;
  }
  public drivers with_certified(String certified) {
    this.certified = certified;
    return this;
  }
  private String wage_plan;
  public String get_wage_plan() {
    return wage_plan;
  }
  public void set_wage_plan(String wage_plan) {
    this.wage_plan = wage_plan;
  }
  public drivers with_wage_plan(String wage_plan) {
    this.wage_plan = wage_plan;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof drivers)) {
      return false;
    }
    drivers that = (drivers) o;
    boolean equal = true;
    equal = equal && (this.driverId == null ? that.driverId == null : this.driverId.equals(that.driverId));
    equal = equal && (this.name == null ? that.name == null : this.name.equals(that.name));
    equal = equal && (this.ssn == null ? that.ssn == null : this.ssn.equals(that.ssn));
    equal = equal && (this.location == null ? that.location == null : this.location.equals(that.location));
    equal = equal && (this.certified == null ? that.certified == null : this.certified.equals(that.certified));
    equal = equal && (this.wage_plan == null ? that.wage_plan == null : this.wage_plan.equals(that.wage_plan));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof drivers)) {
      return false;
    }
    drivers that = (drivers) o;
    boolean equal = true;
    equal = equal && (this.driverId == null ? that.driverId == null : this.driverId.equals(that.driverId));
    equal = equal && (this.name == null ? that.name == null : this.name.equals(that.name));
    equal = equal && (this.ssn == null ? that.ssn == null : this.ssn.equals(that.ssn));
    equal = equal && (this.location == null ? that.location == null : this.location.equals(that.location));
    equal = equal && (this.certified == null ? that.certified == null : this.certified.equals(that.certified));
    equal = equal && (this.wage_plan == null ? that.wage_plan == null : this.wage_plan.equals(that.wage_plan));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.driverId = JdbcWritableBridge.readInteger(1, __dbResults);
    this.name = JdbcWritableBridge.readString(2, __dbResults);
    this.ssn = JdbcWritableBridge.readString(3, __dbResults);
    this.location = JdbcWritableBridge.readString(4, __dbResults);
    this.certified = JdbcWritableBridge.readString(5, __dbResults);
    this.wage_plan = JdbcWritableBridge.readString(6, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.driverId = JdbcWritableBridge.readInteger(1, __dbResults);
    this.name = JdbcWritableBridge.readString(2, __dbResults);
    this.ssn = JdbcWritableBridge.readString(3, __dbResults);
    this.location = JdbcWritableBridge.readString(4, __dbResults);
    this.certified = JdbcWritableBridge.readString(5, __dbResults);
    this.wage_plan = JdbcWritableBridge.readString(6, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(driverId, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(name, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(ssn, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(location, 4 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(certified, 5 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(wage_plan, 6 + __off, 12, __dbStmt);
    return 6;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(driverId, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(name, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(ssn, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(location, 4 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(certified, 5 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(wage_plan, 6 + __off, 12, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.driverId = null;
    } else {
    this.driverId = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.name = null;
    } else {
    this.name = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.ssn = null;
    } else {
    this.ssn = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.location = null;
    } else {
    this.location = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.certified = null;
    } else {
    this.certified = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.wage_plan = null;
    } else {
    this.wage_plan = Text.readString(__dataIn);
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.driverId) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.driverId);
    }
    if (null == this.name) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, name);
    }
    if (null == this.ssn) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, ssn);
    }
    if (null == this.location) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, location);
    }
    if (null == this.certified) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, certified);
    }
    if (null == this.wage_plan) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, wage_plan);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.driverId) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.driverId);
    }
    if (null == this.name) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, name);
    }
    if (null == this.ssn) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, ssn);
    }
    if (null == this.location) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, location);
    }
    if (null == this.certified) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, certified);
    }
    if (null == this.wage_plan) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, wage_plan);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(driverId==null?"null":"" + driverId, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(name==null?"null":name, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(ssn==null?"null":ssn, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(location==null?"null":location, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(certified==null?"null":certified, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(wage_plan==null?"null":wage_plan, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(driverId==null?"null":"" + driverId, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(name==null?"null":name, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(ssn==null?"null":ssn, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(location==null?"null":location, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(certified==null?"null":certified, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(wage_plan==null?"null":wage_plan, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.driverId = null; } else {
      this.driverId = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.name = null; } else {
      this.name = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.ssn = null; } else {
      this.ssn = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.location = null; } else {
      this.location = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.certified = null; } else {
      this.certified = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.wage_plan = null; } else {
      this.wage_plan = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.driverId = null; } else {
      this.driverId = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.name = null; } else {
      this.name = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.ssn = null; } else {
      this.ssn = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.location = null; } else {
      this.location = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.certified = null; } else {
      this.certified = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.wage_plan = null; } else {
      this.wage_plan = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    drivers o = (drivers) super.clone();
    return o;
  }

  public void clone0(drivers o) throws CloneNotSupportedException {
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("driverId", this.driverId);
    __sqoop$field_map.put("name", this.name);
    __sqoop$field_map.put("ssn", this.ssn);
    __sqoop$field_map.put("location", this.location);
    __sqoop$field_map.put("certified", this.certified);
    __sqoop$field_map.put("wage_plan", this.wage_plan);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("driverId", this.driverId);
    __sqoop$field_map.put("name", this.name);
    __sqoop$field_map.put("ssn", this.ssn);
    __sqoop$field_map.put("location", this.location);
    __sqoop$field_map.put("certified", this.certified);
    __sqoop$field_map.put("wage_plan", this.wage_plan);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
